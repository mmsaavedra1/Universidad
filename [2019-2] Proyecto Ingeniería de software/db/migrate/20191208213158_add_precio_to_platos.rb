class AddPrecioToPlatos < ActiveRecord::Migration[5.2]
  def change
    add_column :platos, :precio, :integer
  end
end
