class CreateRestaurantes < ActiveRecord::Migration[5.2]
  def change
    create_table :restaurantes do |t|
      t.string :nombre
      t.string :correo
      t.text :direccion
      t.integer :valoracion
      t.string :numero_telefono

      t.timestamps
    end
  end
end
