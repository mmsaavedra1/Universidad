class BorrandoNombres < ActiveRecord::Migration[5.2]
  def change
    remove_column :restaurantes, :email_propietario
  end
end
