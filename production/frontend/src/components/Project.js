import React from 'react';
import { Link } from 'react-router-dom';

const ProjectItem = ({ project, deleteProject }) => {
    return (
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                <Link to={`/project/${project.name}/`}>{project.name}</Link>
            </td>
            <td>
                {project.users}
            </td>
            <td>
                {project.repoUrl}
            </td>
            <td><button onClick={() => deleteProject(project.id)} type='button'>Delete</button></td>
        </tr>
    )
}


const ProjectList = ({ projects, deleteProject }) => {
    return (
        <div className='projects-list'>
            <table>
                <thead>
                    <tr><th>PROJECTS</th></tr>
                    <tr>
                        <th>ID</th>

                        <th>Name</th>

                        <th>Users (IDs)</th>

                        <th>Repository</th>

                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {projects.map((project) => <ProjectItem
                        key={project.name}
                        project={project}
                        deleteProject={deleteProject} />)}
                </tbody>
            </table>
            <Link to='/projects/create'>Create</Link>
        </div>
    )
}

export default ProjectList;
