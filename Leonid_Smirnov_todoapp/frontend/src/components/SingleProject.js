import React from 'react'
import { useParams } from 'react-router-dom'


const ProjectItem = ({ project }) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.users}</td>
            <td>{project.repoUrl}</td>
        </tr>
    )

}

const SingleProjectItem = ({ projects }) => {

    let { name } = useParams();
    let filtered_projects = projects.filter((project) => project.name === name)
    return (
        <table>
            <tr>
                <th>NAME</th>
                <th>USERS</th>
                <th>REPOSITORY</th>
            </tr>
            {filtered_projects.map((project) => <ProjectItem key={project.name} project={project} />)}
        </table>
    )
}

export default SingleProjectItem;

