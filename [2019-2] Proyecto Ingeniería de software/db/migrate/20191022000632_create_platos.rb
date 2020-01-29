class CreatePlatos < ActiveRecord::Migration[5.2]
  def change
    create_table :platos do |t|
      t.string :nombre
      t.text :descripcion
      t.integer :cantidad_personas_sugeridas
      t.integer :valoracion

      t.timestamps
    end
  end
end
