'use strict'

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var ElementoSchema = Schema({
	num_individuo: Number,
	especie: Number,
	coordX: Number,
	coordY: Number,
	orientacion: Number
});

module.exports = mongoose.model('Elemento', ElementoSchema);