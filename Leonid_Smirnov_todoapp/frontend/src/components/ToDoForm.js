import React from 'react'


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = { text: '', isActive: true, project: props.projects[0].id, user: props.users[0].id }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createToDo(this.state.text, this.state.isActive, this.state.project, this.state.user)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">text</label>
                    <input type="text" className="form-control" name="text" value={this.state.text} onChange={(event) => this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="isActive">active</label>
                    <input type="checkbox" checked="checked" className="form-control" name="isActive" value={this.state.isActive} onChange={(event) => this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="project">project</label>
                    <select name="project" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.projects.map((project) => <option value={project.id}>{project.name}</option>)}
                    </select>
                </div>
                <div className="form-group">
                    <label for="user">user</label>
                    <select name="user" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.users.map((user) => <option value={user.id}>{user.username}</option>)}
                    </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}

export default ToDoForm