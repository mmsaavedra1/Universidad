class CambiandoNombres < ActiveRecord::Migration[5.2]
  def change
    rename_column :reviews, :id_restaurante, :restaurante_id
    rename_column :reviews, :id_user, :user_id
  end
end
