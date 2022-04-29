import React from 'react'


const ProjectItem = ({item}) => {
	return (
		<tr>
			<td>
				{projectapp.name}
			</td>
			<td>
				{projectapp.link}
			</td>
			<td>
				{projectapp.user}
			</td>
		</tr>
	)
}
const ProjectList = ({items}) => {
	return (
		<table>
			<th>
				NAME
			</th>
			<th>
				LINK
			</th>
			<th>
				USER
			</th>
			{items.map((item) => <ProjectItem item={item} />)}
		</table>
	)
}

export default ProjectList
