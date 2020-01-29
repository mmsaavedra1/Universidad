class Restaurante < ApplicationRecord
  has_many :platos
  has_many :reviews

  has_attached_file :restaurante_img, {styles: { :medium => "240x240>", :small => "150x150>" },
                                       :path => ":rails_root/public/assets/images/restaurantes/:id/:style/:basename.:extension",
                                       :url  => "/assets/images/restaurantes/:id/:style/:basename.:extension",
                                       :default_url => "sin_foto/:style/missing.png"}

  validates_attachment_content_type :restaurante_img, content_type: /\Aimage\/.*\z/

  def self.search(search)
    if search
      @restaurantes = Restaurante.all.where('nombre LIKE ?', "%#{search}%")
    else
      @restaurantes = Restaurante.all
    end
  end


end
