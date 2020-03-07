const express = require('express');
const app = express();
const mysql = require('mysql');
const bodyparser = require('body-parser');
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({ extended: false }));

const con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database:"newdb"
});


app.get('/', function (req, res) {
    res.sendFile( __dirname + "/" + "demo.html" );
})


app.post('/create', (req, res) => {
    var name = req.body.name;
    var regno = req.body.regno;
    var phone = req.body.phone;
    var query = 'INSERT INTO USER (name,regno,phone) VALUES ("' + name + '","' + regno + '","' + phone + '")';
    con.query(query, (err, results) => {
        if (err) res.send(err);
        else {
            console.log("Created");
            res.send("User created");
        }

    })
})


app.post('/delete', (req, res) => {
    var id = req.body.id;
    var query = 'DELETE FROM user WHERE id =  ("' + id + '")';
    con.query(query, (err, results) => {
        if (err) res.send(err);
        else {
            console.log("Deleted");
            res.send("User deleted");
        }

    })
})


app.post('/update', (req, res) => {
    var id = req.body.id;
    var name = req.body.name;
    var regno = req.body.regno;
    var phone = req.body.phone;
    var query = 'UPDATE user SET name="' + name + '" , regno="' + regno + '", phone="' + phone + '" WHERE id=("' + id + '")';
    con.query(query, (err, results) => {
        if (err) res.send(err);
        else {
            console.log("Updated");
            res.send("User data Updated");
        }

    })
})

const port = 5000;

app.listen(port, () =>
    console.log("App listening on 5000")
);