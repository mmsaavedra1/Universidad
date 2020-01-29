class Plato < ApplicationRecord
  belongs_to :restaurante
  has_many :users
  has_many :plato_reviews
  has_many :ordens

  has_attached_file :plato_img, {styles: {:medium => "240x240>", :small => "150x150>" },
                                 :url  => "/assets/images/platos/:id/:style/:basename.:extension",
                                 :default_url => "sin_foto/:style/missing.png"}

  validates_attachment_content_type :plato_img, content_type: /\Aimage\/.*\z/
end
