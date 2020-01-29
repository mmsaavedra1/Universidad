class ArreglarOrden < ActiveRecord::Migration[5.2]
  def change
    remove_column :ordens, :datetime
    remove_column :ordens, :hora_llegada
    add_column :ordens, :hora_llegada, :datetime
  end
end
