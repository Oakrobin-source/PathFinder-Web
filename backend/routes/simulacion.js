'use strict'

var express = require('express');
var SimulacionController = require('../controllers/simulacion');

var router = express.Router();

var multipart = require('connect-multiparty');

/* GET home page. */
/*router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});*/

router.get('/simulacion/:cof1/:cof2?/:cof3?/:cof4?/:cof5?/:cof6?/:cof7?/:cof8?/:cof9?',SimulacionController.simulacion);

module.exports = router;
