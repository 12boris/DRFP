import React from 'react'
import usersList from './components/users.js'
import ToDOList from './components/ToDO.js'
import ProjectList from './components/Project.js'
import LoginForm from './components/Auth.js'


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
	
	
	load_data() {
		const headers = this.get_headers()
		axios.get('http://127.0.0.1:8000/api/authors/', {headers}).then(response => {
			this.setState({authors: response.data})
		}).catch(error => console.log(error))
		axios.get('http://127.0.0.1:8000/api/books/', {headers}).then(response => {
			this.setState({books: response.data})
		}).catch(error => {
			console.log(error)
			this.setState({books: []})
		})
	}
	
	set_token(token) {
		const cookies = new Cookies()
		cookies.set('token', token)
		this.setState({'token': token}, ()=>this.load_data())
	}
	
	is_authenticated() {
		return this.state.token != ''
	}
	
	logout() {
		this.set_token('')
	}
	
	get_token_from_storage() {
		const cookies = new Cookies()
		const token = cookies.get('token')
		this.setState({'token': token}, ()=>this.load_data())
	}
	
	get_token(username, password) {
		axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,
		password: password}).then(response => {
			this.set_token(response.data['token'])
		}).catch(error => alert('Неверный логин или пароль'))
	}
	
	componentDidMount() {
		this.get_token_from_storage()
	}
	
	get_headers() {
		let headers = {
			'Content-Type': 'application/json'
		}
		if (this.is_authenticated())
			{
			headers['Authorization'] = 'Token ' + this.state.token
			}
		return headers
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
						<li>
						<li>
							{this.is_authenticated() ? <button
							onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
						</li>
					</ul>
				</nav>
<Switch>
	<Route exact path='/' component={() => <UsersList items={this.state.users} />} />
	<Route exact path='/ToDos' component={() => <ToDoList items={this.state.ToDos} />} />
	<Route exact path='/Projects' component={() => <ProjectList items={this.state.Projects} />} />
	<Route exact path='/login' component={() => <LoginForm />} />
	<Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
	<Redirect from='/users' to='/' />
	<Route component={NotFound404} />
</Switch>
				</HashRouter>
			</div>
		)
	}
}

get_token(username, password) {
	axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,
	password: password})
	.then(response => {
		console.log(response.data)
	}).catch(error => alert('Неверный логин или пароль'))
}

export default App;
