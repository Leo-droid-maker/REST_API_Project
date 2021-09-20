import React from "react";

const UserItem = ({ user }) => {
    return (
        <tr>
            <td>
                {user.id}
            </td>
            <td>
                {user.username}
            </td>
            <td>
                {user.firstName}
            </td>
            <td>
                {user.lastName}
            </td>
            <td>
                {user.email}
            </td>

        </tr>
    )
}


const UserList = ({ users }) => {
    return (
        <table>
            <thead>
                <tr><th>USERS</th></tr>
                <tr>
                    <th>User ID</th>

                    <th>Username</th>

                    <th>First name</th>

                    <th>Last name</th>

                    <th>Email</th>

                </tr>
            </thead>
            <tbody>
                {users.map((user) => <UserItem key={user.id} user={user} />)}
            </tbody>
        </table>
    )
}

export default UserList;