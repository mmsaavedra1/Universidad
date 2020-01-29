class AddAttachmentPlatoImgToPlatos < ActiveRecord::Migration[5.2]
  def self.up
    change_table :platos do |t|
      t.attachment :plato_img
    end
  end

  def self.down
    remove_attachment :platos, :plato_img
  end
end
