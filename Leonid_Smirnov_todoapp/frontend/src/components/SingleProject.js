import React from 'react'
import { useParams } from 'react-router-dom'


const ProjectItem = ({ project }) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.users}</td>
            <td>{project.repoUrl}</td>
        </tr>
    )

}

const SingleProjectItem = ({ projects }) => {

    let { id } = useParams();
    let filtered_projects = projects.filter((project) => project.id === +id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>USERS</th>
                <th>REPOSITORY</th>
            </tr>
            {filtered_projects.map((project) => <ProjectItem key={project.id} project={project} />)}
        </table>
    )
}

export default SingleProjectItem;

