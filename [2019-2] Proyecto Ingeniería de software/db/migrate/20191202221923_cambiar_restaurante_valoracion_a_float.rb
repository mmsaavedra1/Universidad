class CambiarRestauranteValoracionAFloat < ActiveRecord::Migration[5.2]
  def change
    change_column :restaurantes, :valoracion, :float
  end
end
