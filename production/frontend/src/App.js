import './App.css';
import React from "react"
import UserList from './components/User';
import ProjectList from './components/Project';
import ToDoList from './components/ToDo';
import SingleProjectItem from './components/SingleProject';
import ProjectForm from './components/ProjectForm';
import ToDoForm from './components/ToDoForm';
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

const API_ROOT = 'http://80.78.253.197:8000/api/'
const getUrl = (url_name) => `${API_ROOT}${url_name}`


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
      .post('http://80.78.253.197:8000/api/token-auth/', {
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
    // const API_ROOT = 'http://127.0.0.1:8000/api/'
    // const getUrl = (url_name) => `${API_ROOT}${url_name}`
    const URLs = [
      getUrl('users/'),
      getUrl('projects/'),
      getUrl('todos/')
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

  createProject(name, repoUrl, user) {
    console.log(name, repoUrl, user)
    const headers = this.getHeaders()
    const data = { name: name, repoUrl: repoUrl, users: [user], }
    axios
      .post(`http://80.78.253.197:8000/api/projects/`, data, { headers })
      .then(response => {
        let newProject = response.data
        // console.log('project here', newProject)
        // console.log('user here', user)
        // newProject['users'].push(user)
        this.setState(
          {
            projects: [...this.state.projects, newProject]
          }
        )
      })
      .catch(error => console.log(error))
  }

  createToDo(text, isActive, project, user) {
    console.log(text, isActive, project, user)
    const headers = this.getHeaders()
    const data = { text: text, isActive: isActive, project: project, user: user }
    console.log('data is here', data)
    axios
      .post(`http://80.78.253.197:8000/api/todos/`, data, { headers })
      .then(response => {
        let newToDo = response.data
        console.log('todo here', newToDo)
        this.setState(
          {
            todos: [...this.state.todos, newToDo]
          }
        )
      })
      .catch(error => console.log(error))
  }

  deleteProject(id) {
    const headers = this.getHeaders()
    const url = getUrl(`projects/${id}/`)
    axios
      .delete(url, { headers })
      .then(response => {
        this.setState(
          {
            projects: this.state.projects.filter((project) => project.id !== id)
          }
        )
      })
      .catch(error => console.log(error))
    console.log('delete', id)
  }

  deleteToDo(id) {
    const headers = this.getHeaders()
    const url = getUrl(`todos/${id}/`)
    axios
      .delete(url, { headers })
      .then(response => {
        this.setState(
          {
            todos: this.state.todos.filter((todo) => todo.id !== id)
          }
        )
      })
      .catch(error => console.log(error))
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
            <Route exact path='/projects/create' component={() => <ProjectForm
              users={this.state.users}
              createProject={(name, repoUrl, user) => this.createProject(name, repoUrl, user)} />} />
            <Route exact path='/projects' component={() => <ProjectList
              projects={this.state.projects}
              deleteProject={(id) => this.deleteProject(id)} />} />
            <Route exact path='/todos' component={() => <ToDoList
              todos={this.state.todos}
              deleteToDo={(id) => this.deleteToDo(id)} />} />
            <Route exact path='/todos/create' component={() => <ToDoForm
              projects={this.state.projects}
              users={this.state.users}
              createToDo={(text, isActive, project, user) => this.createToDo(text, isActive, project, user)} />} />
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
