var express = require('express');
var admin = require('firebase-admin');
var bodyParser = require('body-parser');

var serviceAccount = require("./service.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://fir-auth-ad1e5.firebaseio.com"
});

var app = express();

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

var hostname = 'localhost';
var port = process.env.PORT || 8080; // set our port
var router = express.Router(); // get an instance of the express Router
var defaultAuth = admin.auth();

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/', function(req, res) {
  res.json({message: 'Yo, a get.'});
});

router.post('/', function(req, res) {
  console.log(req.query)
  defaultAuth.createUser({
    email: "user@example.com",
    emailVerified: false,
    password: "secretPassword",
    displayName: "John Doe",
    photoURL: "http://www.example.com/12345678/photo.png",
    disabled: false
  }).then(function(userRecord) {
    console.log("Successfully created new user:", userRecord.uid);
  }).catch(function(error) {
    console.log("Error creating new user:", error);
  });
  res.json({message: 'Yo, a post!'});
})

// more routes for our API will happen here

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
