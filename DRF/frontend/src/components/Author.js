import React from 'react'
const UserItem = ({user}) => {
	return (
	<tr>
		<td>
			{users.first_name}
		</td>
		<td>
			{users.last_name}
		</td>
		<td>
			{users.birthday_year}
		</td>
		<td>
			{users.email}
		</td>
	</tr>
	)
}
const UsersList = ({users}) => {
	return (
		<table>
			<th>
				First name
			</th>
			<th>
				Last Name
			</th>
			<th>
				Birthday year
			</th>
			<th>
				Email
			</th>
			{users.map((user) => <UsersItem user={user} />)}
		</table>
	)
}

export default UsersList
