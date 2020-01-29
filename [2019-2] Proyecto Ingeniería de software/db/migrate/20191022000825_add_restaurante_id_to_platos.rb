class AddRestauranteIdToPlatos < ActiveRecord::Migration[5.2]
  def change
    add_column :platos, :restaurante_id, :integer
  end
end
