class AddEstadoToResturantes < ActiveRecord::Migration[5.2]
  def change
    add_column :restaurantes, :estado, :string
  end
end
