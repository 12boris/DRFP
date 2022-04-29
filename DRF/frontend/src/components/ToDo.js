import React from 'react'


const ToDoItem = ({item}) => {
	return (
		<tr>
			<td>{item.ToDoapp.project}</td>
			<td>{item.ToDoapp.is_staff}</td>
			<td>{item.ToDoapp.text}</td>
			<td>{item.ToDoapp.create_at}</td>
			<td>{item.ToDoapp.update_at}</td>
			<td>{item.ToDoapp.user}</td>
			<td>{item.ToDoapp.active}</td>
		</tr>
	)
}

const ToDoList = ({items}) => {
	return (
		<table>
			<tr>
				<th>PROJECT</th>
				<th>IS STAFF</th>
				<th>TEXT</th>
				<th>CREATE AT YEAR</th>
				<th>UPDATE AT</th>
				<th>USER</th>
				<th>ACTIVE</th>
			</tr>
			{items.map((item) => <ToDoItem item={item} />)}
		</table>
	)
}
export default ToDoList
