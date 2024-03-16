const {useState} = React;

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            mylist: ["Mohammad Safa Kamali", "Person 2", "Person 3", "Person 4"],
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