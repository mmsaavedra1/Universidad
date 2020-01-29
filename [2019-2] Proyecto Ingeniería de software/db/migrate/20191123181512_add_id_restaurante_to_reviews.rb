class AddIdRestauranteToReviews < ActiveRecord::Migration[5.2]
  def change
    add_column :reviews, :id_restaurante, :integer
  end
end
