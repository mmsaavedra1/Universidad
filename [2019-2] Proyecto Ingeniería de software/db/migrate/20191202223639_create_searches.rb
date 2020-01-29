class CreateSearches < ActiveRecord::Migration[5.2]
  def change
    create_table :searches do |t|
      t.string :keyword
      t.string :ubicacion
      t.integer :min_rating
      t.integer :max_rating

      t.timestamps
    end
  end
end
