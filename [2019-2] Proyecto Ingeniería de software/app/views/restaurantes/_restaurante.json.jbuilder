json.extract! restaurante, :id, :nombre, :correo, :direccion, :valoracion, :numero_telefono, :created_at, :updated_at
json.url restaurante_url(restaurante, format: :json)
