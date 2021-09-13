import React from 'react';
import { Link } from 'react-router-dom';

const ProjectItem = ({ project }) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${project.name}/`}>{project.name}</Link>
            </td>
            <td>
                {project.users}
            </td>
            <td>
                {project.repoUrl}
            </td>
        </tr>
    )
}


const ProjectList = ({ projects }) => {
    return (
        <table>
            <thead>
                <tr><th>PROJECTS</th></tr>
                <tr>
                    <th>Name</th>

                    <th>Users</th>

                    <th>Repository</th>
                </tr>
            </thead>
            <tbody>
                {projects.map((project) => <ProjectItem key={project.name} project={project} />)}
            </tbody>
        </table>
    )
}

export default ProjectList;
