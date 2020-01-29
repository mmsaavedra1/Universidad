class CambiarPlatoValoracionAFloat < ActiveRecord::Migration[5.2]
  def change
    change_column :platos, :valoracion, :float
  end
end
