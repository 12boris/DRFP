import React from 'react'
import usersList from './components/users.js'
import ToDOList from './components/ToDO.js'
import ProjectList from './components/Project.js'
class App extends React.Component {
	constructor(props) {
	
		super(props)
		const user1 = {first_name: "Boris", last_name: "Igdal", birthday_year: 1880, email: "asa@asas.ru"}
		const users = [user1]
		
		const ToDo1 = {project: "DRF", is_staff: "True", text: "sdsssds", create_at: "02.13", update_at: "02.14", user: "Boris", active: "True"}
		const ToDos = [ToDo1]
		
		const Project1 = {name: "DRF", link: "https://dfd/sds/ds", user: "boris"}
		const Projects = [Project1]
		
		this.state = {
			'users': users,
			'ToDos': ToDos,
			'Projects': Projects
		}
	
	}
	render() {
		return (
			<div className="App">
				<AuthorList items={this.state.authors} />
				<ToDosList items={this.state.ToDos} />
				<ProjectsList items={this.state.Projects} />
			</div>
		)
	}
}


<Switch>
	<Route exact path='/' component={() => <UsersList items={this.state.users} />} />
	<Route exact path='/ToDos' component={() => <ToDoList items={this.state.ToDos} />} />
	<Route exact path='/Projects' component={() => <ProjectList items={this.state.Projects} />} />
	<Redirect from='/users' to='/' />
	<Route component={NotFound404} />
</Switch>







import {HashRouter, Route, Link, Switch} from 'react-router-dom'


const NotFound404 = ({ location }) => {
	return (
		<div>
			<h1>Страница по адресу '{location.pathname}' не найдена</h1>
		</div>
	)
}
class App extends React.Component {
	render() {
		return (
			<div className="App">
				<HashRouter>
				<nav>
					<ul>
						<li>
							<Link to='/'>Authors</Llink>
						</li>
						<li>
							<Link to='/ToDos'>ToDos</Link>
						</li>
						<li>
							<Link to='/Projects'>Projects</Link>
						</li>
					</ul>
				</nav>
<Switch>
	<Route exact path='/' component={() => <UsersList items={this.state.users} />} />
	<Route exact path='/ToDos' component={() => <ToDoList items={this.state.ToDos} />} />
	<Route exact path='/Projects' component={() => <ProjectList items={this.state.Projects} />} />
	<Redirect from='/users' to='/' />
	<Route component={NotFound404} />
</Switch>
				</HashRouter>
			</div>
		)
	}
}


export default App;
