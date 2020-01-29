class BorrarEstados < ActiveRecord::Migration[5.2]
  def change
    remove_column :restaurantes, :estado
  end
end
