#!/bin/bash

if ["$VIRTUAL_ENV" != ""]
then
echo "No hay un venv activo, activando..."
source  ./venv/bin/activate
echo "venv $VIRTUAL_ENV"
echo "venv activado"
fi

echo "Corriendo tests..."
python3 -m unittest tests/tests*.py