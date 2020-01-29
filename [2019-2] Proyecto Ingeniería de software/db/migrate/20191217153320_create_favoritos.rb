class CreateFavoritos < ActiveRecord::Migration[5.2]
  def change
    create_table :favoritos do |t|
      t.integer :user_id
      t.integer :restaurante_id

      t.timestamps
    end
  end
end
