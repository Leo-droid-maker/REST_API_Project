import './App.css';
import React from "react"
import UserList from './components/User';
import ProjectList from './components/Project';
import ToDoList from './components/ToDo';
import SingleProjectItem from './components/SingleProject';
import axios from 'axios';
import Footer from './components/Footer';
import Menu from './components/Menu';
import { BrowserRouter, Route, Link, Switch, Redirect } from 'react-router-dom'

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
      'todos': []
    }
  }

  async componentDidMount() {

    const API_ROOT = 'http://127.0.0.1:8000/api/'
    const get_url = (url_name) => `${API_ROOT}${url_name}`
    const URLs = [
      get_url('users'),
      get_url('projects'),
      get_url('todos')
    ]
    const requests = URLs.map(URL => axios.get(URL).catch(error => null));

    try {
      const [users, projects, todos] = await axios.all(requests);
      this.setState(
        {
          'users': users.data.results,
          'projects': projects.data.results,
          'todos': todos.data.results
        }
      );
    }
    catch (error) {
      console.log(error.message);
    }
  }


  // componentDidMount() {

  //   axios.all(
  //     [
  //       axios.get(get_url('users')),
  //       axios.get(get_url('projects')),
  //       axios.get(get_url('todos'))
  //     ]
  //   )
  //     .then(axios.spread((users, projects, todos) => {
  //       this.setState(
  //         {
  //           'users': users.data.results,
  //           'projects': projects.data.results,
  //           'todos': todos.data.results
  //         }
  //       )
  //     }))
  //     .catch(error => console.log(error))
  // }

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
            </ul>
          </nav>
          <Switch>
            <Route exact path='/' component={() => <UserList users={this.state.users} />} />
            <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
            <Route exact path='/todos' component={() => <ToDoList todos={this.state.todos} />} />
            <Route path="/project/:id">
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
