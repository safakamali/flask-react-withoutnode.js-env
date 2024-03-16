const {useState} = React;

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            mylist: ["Mohammad Safa Kamali", "Fatemeh Taghavi", "Sajjad Kamali", "Mohammad Kamali"],
            alert: ''
        };
    }

    render() {
        return (
            <div>
                <h1>The Food Store is here</h1>
                <span>{this.state.alert}</span>
                <ul>
                    {this.state.mylist.map((item, _index) =>
                        <li onClick={() => {
                            this.setState({alert: 'Item ' + item + ' selected'})
                        }}>{item}</li>
                    )}
                </ul>
            </div>
        );
    }
}