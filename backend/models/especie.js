'use strict'

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var EspecieSchema = Schema({
	ratio_mutacion: Number,
	color: String,
	score: Number
});

module.exports = mongoose.model('Especie', EspecieSchema);