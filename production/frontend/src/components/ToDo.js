import React from 'react';
import { Link } from 'react-router-dom';

const ToDoItem = ({ todo, deleteToDo }) => {
    return (
        <tr>
            <td>
                {todo.id}
            </td>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.created}
            </td>
            <td>
                {todo.updated}
            </td>
            <td>
                {todo.user}
            </td>
            <td><button onClick={() => deleteToDo(todo.id)} type='button'>Delete</button></td>
        </tr>
    )
}


const ToDoList = ({ todos, deleteToDo }) => {
    return (
        <div className='todos-list'>
            <table>
                <thead>
                    <tr><th>TODOS</th></tr>
                    <tr>
                        <th>ID</th>

                        <th>Project</th>

                        <th>Text</th>

                        <th>Created</th>

                        <th>Updated</th>

                        <th>User</th>
                    </tr>
                </thead>
                <tbody>
                    {todos.map((todo) => <ToDoItem
                        key={todo.id}
                        todo={todo}
                        deleteToDo={deleteToDo} />)}
                </tbody>
            </table>
            <Link to='/todos/create'>Create</Link>
        </div>
    )
}

export default ToDoList;