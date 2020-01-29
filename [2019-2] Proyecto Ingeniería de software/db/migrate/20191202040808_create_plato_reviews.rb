class CreatePlatoReviews < ActiveRecord::Migration[5.2]
  def change
    create_table :plato_reviews do |t|
      t.integer :rating
      t.text :comentario
      t.integer :user_id
      t.integer :plato_id

      t.timestamps
    end
  end
end
