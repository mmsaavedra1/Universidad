class AddAttachmentRestauranteImgToRestaurantes < ActiveRecord::Migration[5.2]
  def self.up
    change_table :restaurantes do |t|
      t.attachment :restaurante_img
    end
  end

  def self.down
    remove_attachment :restaurantes, :restaurante_img
  end
end
