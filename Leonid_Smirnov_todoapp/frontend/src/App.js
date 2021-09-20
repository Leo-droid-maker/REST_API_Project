import './App.css';
import React from "react"
import UserList from './components/User';
import ProjectList from './components/Project';
import ToDoList from './components/ToDo';
import SingleProjectItem from './components/SingleProject';
import LoginForm from './components/Auth';
import axios from 'axios';
import Footer from './components/Footer';
import Menu from './components/Menu';
import { BrowserRouter, Route, Link, Switch, Redirect } from 'react-router-dom';
import Cookies from 'universal-cookie';

const NotFound404 = ({ location }) => {
  return (
    <div>
      <h1>Page on path '{location.pathname}' not found</h1>
    </div>
  )
}


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      'users': [],
      'projects': [],
      'todos': [],
      'token': ''
    }
  }

  setToken(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState(
      { 'token': token }, () => this.loadData()
    )
  }

  isAuthenticated() {
    return !!this.state.token
  }

  logout() {
    this.setToken('')
  }

  getTokenFromStorage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState(
      { 'token': token }, () => this.loadData()
    )
  }

  getToken(username, password) {
    axios
      .post('http://127.0.0.1:8000/api/token-auth/', {
        username: username,
        password: password
      })
      .then(response => {
        this.setToken(response.data['token'])
      })
      .catch(error => alert('Неверный логин или пароль'))
  }

  getHeaders() {
    let headers = {
      'Content-Type': 'application/json'
      // 'Accept': 'application/json; version=2.0'
    }
    if (this.isAuthenticated()) {
      headers['Authorization'] = `Token ${this.state.token}`
    }
    return headers
  }

  async loadData() {
    const headers = this.getHeaders()
    const API_ROOT = 'http://127.0.0.1:8000/api/'
    const getUrl = (url_name) => `${API_ROOT}${url_name}`
    const URLs = [
      getUrl('users'),
      getUrl('projects'),
      getUrl('todos')
    ]
    const requests = URLs.map(URL => axios.get(URL, { headers }).catch(error => null));

    try {
      const [users, projects, todos] = await axios.all(requests);
      this.setState(
        {
          'users': users.data.results,
          'projects': projects.data.results,
          'todos': todos.data.results,
        }
      );
    }
    catch (error) {
      console.log(error.message);
      this.setState({ 'projects': [] })
    }
  }


  componentDidMount() {
    this.getTokenFromStorage()
  }

  render() {
    return (
      <div className="App">
        <Menu />
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to='/'>Users</Link>
              </li>
              <li>
                <Link to='/projects'>Projects</Link>
              </li>
              <li>
                <Link to='/todos'>ToDos</Link>
              </li>
              <li>
                {this.isAuthenticated() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/' component={() => <UserList users={this.state.users} />} />
            <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
            <Route exact path='/todos' component={() => <ToDoList todos={this.state.todos} />} />
            <Route exact path='/login' component={() => <LoginForm getToken={(username, password) => this.getToken(username, password)} />} />
            <Route path="/project/:name">
              <SingleProjectItem projects={this.state.projects} />
            </Route>
            <Redirect from='/users' to='/' />
            <Route component={NotFound404} />
          </Switch>
        </BrowserRouter>
        <Footer />
      </div>
    );
  }
}

export default App;
