class App {
    constructor(props) {
        super(props);
        this.state = {count: 0};
    }
    handleClick(name) {
        this.setState({name: name});
        
    }
    handleCount(count) {
        this.setState({count: this.state.count + 1});
    }
    render() {
        return (
            <div>
                <h1> Hello {this.state.count}</h1>
                <h1> {this.state.count}</h1>
                <button onClick = {() => {this.handleClick("Dhafi")}}>Dhafi</button>
               <button onClick = {() => {this.handleClick("Alif")}}>Alif</button>
               <button onClick = {() => {this.handleCount()}}>+</button>
            </div>
        );
    }
}