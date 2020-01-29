class AddRestauranteIdToOrdens < ActiveRecord::Migration[5.2]
  def change
    add_column :ordens, :restaurante_id, :integer
  end
end
