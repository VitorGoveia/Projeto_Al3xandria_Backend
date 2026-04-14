class GameDomain:
    def __init__(self, nome, imagem, slug_name, meta_score, url_meta_score, release_date, website, description, rawg_id):
        self.nome = nome
        self.imagem = imagem
        self.slug_name = slug_name
        self.meta_score = meta_score
        self.url_meta_score = url_meta_score
        self.release_date = release_date
        self.website = website
        self.description = description
        self.rawg_id = rawg_id

    
    def to_dict(self):
        return {
            "nome": self.nome,
            "imagem": self.imagem,
            "slug_name": self.slug_name,
            "meta_score": self.meta_score,
            "url_meta_score": self.url_meta_score,
            "release_date": self.release_date,
            "website": self.website,
            "description": self.description,
            "rawg_id": self.rawg_id
        }