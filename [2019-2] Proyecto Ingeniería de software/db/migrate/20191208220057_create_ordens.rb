class CreateOrdens < ActiveRecord::Migration[5.2]
  def change
    create_table :ordens do |t|
      t.integer :plato_id
      t.integer :user_id
      t.integer :precio
      t.string :direccion_de_envio
      t.string :hora_llegada
      t.string :datetime
      t.string :estado
      t.string :notas

      t.timestamps
    end
  end
end
