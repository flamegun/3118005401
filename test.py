import unittest
import calculation

class NewTest(unittest.TestCase):
    def test_txt_add(self):
        print("orig_0.8_add.txt的相似度 ")

        file = open("C:\\Users\\ids\\Desktop\\test\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("C:\\Users\\ids\\Desktop\\test\\orig_0.8_add.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_del(self):
        print("orig_0.8_del.txt的相似度 ")

        file = open("C:\\Users\\ids\\Desktop\\test\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("C:\\Users\\ids\\Desktop\\test\\orig_0.8_del.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_dis_1(self):
        print("orig_0.8_dis_1.txt的相似度 ")

        file = open("C:\\Users\\ids\\Desktop\\test\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("C:\\Users\\ids\\Desktop\\test\\orig_0.8_dis_1.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_dis_10(self):
        print("orig_0.8_dis_10.txt的相似度 ")

        file = open("C:\\Users\\ids\\Desktop\\test\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("C:\\Users\\ids\\Desktop\\test\\orig_0.8_dis_10.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_dis_15(self):
        print("orig_0.8_dis_15.txt的相似度 ")

        file = open("C:\\Users\\ids\\Desktop\\test\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("C:\\Users\\ids\\Desktop\\test\\orig_0.8_dis_15.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

if __name__ == '__main__':

    unittest.main()
