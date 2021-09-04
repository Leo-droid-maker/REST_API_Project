import React from 'react';

const ToDoItem = ({ todo }) => {
    return (
        <tr>
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
        </tr>
    )
}


const ToDoList = ({ todos }) => {
    return (
        <table>
            <thead>
                <tr><th>TODOS</th></tr>
                <tr>
                    <th>Project</th>

                    <th>Text</th>

                    <th>Created</th>

                    <th>Updated</th>

                    <th>User</th>
                </tr>
            </thead>
            <tbody>
                {todos.map((todo) => <ToDoItem key={todo.id} todo={todo} />)}
            </tbody>
        </table>
    )
}

export default ToDoList;