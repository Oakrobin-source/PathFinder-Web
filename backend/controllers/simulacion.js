'use strict'

var Elemento = require('../models/elemento');
var Especie = require('../models/especie');
var fs = require('fs');
var path = require('path');

var controller = {

	simulacion: function(req, res){

		try {
			console.log("entering try block");
	  		var coeficienteEspecie1 = req.params.cof1;
	  		var coeficienteEspecie2 = req.params.cof2;
	  		var coeficienteEspecie3 = req.params.cof3;
	  		var coeficienteEspecie4 = req.params.cof4;
	  		var coeficienteEspecie5 = req.params.cof5;
	  		var coeficienteEspecie6 = req.params.cof6;
	  		var coeficienteEspecie7 = req.params.cof7;
	  		var coeficienteEspecie8 = req.params.cof8;
	  		var coeficienteEspecie9 = req.params.cof9;

			const spawn = require("child_process").spawn;
			console.log("spawn process");

			const pythonProcess = spawn('python3',["./../PythonAI/AI_PathFinder_Especies.py", coeficienteEspecie1, coeficienteEspecie2, coeficienteEspecie3,
				coeficienteEspecie4,coeficienteEspecie5,coeficienteEspecie6,coeficienteEspecie7,coeficienteEspecie8,coeficienteEspecie9]);
			console.log("spawn process 2");

			pythonProcess.stdout.on('data', function(data) {
				//console.log("consola " + data.toString().replace("\n",""));
				//console.log("consola " + 'Proceso finalizado OK');
				if(data.toString().replace("\n","") == 'Proceso finalizado OK'){
					console.log("consola " + data.toString().replace("\n",""));
					res.end('end');
				}else{
					//console.log("Error " + data.toString());
				}
			});

			pythonProcess.stderr.on('data', (data) => {
				console.log(data.toString().replace("\n",""));
			});

		}
		catch (e) {
		  console.log("entering catch block");
		  console.log(e);
		  console.log("leaving catch block");
		}
		finally {
		  console.log("entering and leaving the finally block");
		  return res.status(200);
		}

	}

};

module.exports = controller;