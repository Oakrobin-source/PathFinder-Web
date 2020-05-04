'use strict'

var Elemento = require('../models/elemento');
var fs = require('fs');
var path = require('path');

var controller = {

	getElemento: function(req, res){
		var elementoId = req.params.id;

		if(elementoId == null) return res.status(404).send({message: 'El elemento no existe no existe.'});

		Elemento.findById(elementoId, (err, elemento) => {

			if(err) return res.status(500).send({message: 'Error al devolver los datos.'});

			if(!elemento) return res.status(404).send({message: 'El elemento no existe.'});

			return res.status(200).send({
				elemento
			});

		});
	},

	getElementosPorEspecie: function(req, res){

	},

	getElementos: function(req, res){

		Elemento.find({}).sort({'especie': 1, 'num_individuo': 1}).exec((err, elementos) => {

			if(err) return res.status(500).send({message: 'Error al devolver los datos.'});

			if(!elementos) return res.status(404).send({message: 'No hay elementos que mostrar.'});

			return res.status(200).send({elementos});
		});

	},

	crearElemento: function(req, res){
		var elemento = new Elemento();

		var elemento = req.body;
		elemento.num_individuo = params.num_individuo;
		elemento.especie = params.especie;
		elemento.coordX = params.coordX;
		elemento.coordY = params.coordY;
		elemento.orientacion = params.orientacion;

		elemento.save((err, elementoStored) => {
			if(err) return res.status(500).send({message: 'Error al guardar el documento.'});

			if(!elementoStored) return res.status(404).send({message: 'No se ha podido guardar el elemento.'});

			return res.status(200).send({elemento: elementoStored});
		});
	},

	crearElementosPorEspecie: function(req, res){

	},

	crearElementos: function(req, res){

	}

};

module.exports = controller;