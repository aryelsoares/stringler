#ifndef STRINGLER_HPP
#define STRINGLER_HPP

#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <stdexcept>
#include "info.hpp"

class Stringler {
    public:

    // constructor
    Stringler(std::string& str) {
        for (auto& s : str) {
            (std::isalnum(static_cast<unsigned char>(s)))? s = std::tolower(s) : s = ' ';
        }

        str += ' ';

        std::string temp{};

        for (size_t i{}; i < str.size(); ++i) {
            if (str[i] != ' ') {
                temp += str[i];
            } else {
                if (!temp.empty()) {
                    // stop words
                    bool has_stop_word = false;
                    for (size_t j{}; j < stop_words.size(); ++j) {
                        if (temp == stop_words[j]) {
                            has_stop_word = true;
                            break;
                        }
                    }

                    if (!has_stop_word) {
                        m_arr.push_back(temp);
                    }

                    temp.clear();
                }
            }
        }

        m_size = static_cast<double>(m_arr.size());

        if (m_size == 0.0) {
            throw std::invalid_argument("String must have a valid size");
        }
    }

    // data
    std::vector<std::string> getArr() const {
        return m_arr;
    }

    // tokens
    int getSize() const {
        return static_cast<int>(m_size);
    }

    // largest
    std::string largest() const {
        std::string max{};
        for (const auto& word : m_arr) {
            if (word.size() > max.size()) {
                max = word;
            }
        }
        return max;
    }

    // mean
    double mean() const {
        double count{};
        for (const auto& word : m_arr) {
            count += word.size();
        }
        return count / static_cast<double>(m_size);
    }

    // std
    double std() const {
        double count{};
        for (const auto& word : m_arr) {
            count += std::pow(word.size() - mean(), 2);
        }
        return std::sqrt(count / m_size);
    }

    // skew
    double skew() const {
        double sum = 0.0;
        double mu = mean();
        double sigma = std();
        for (const auto& s : m_arr) {
            sum += std::pow((s.size() - mu) / sigma, 3);
        }
        return sum / m_size;
    }

    // kurtosis
    double kurtosis() const {
        double sum = 0.0;
        double mu = mean();
        double sigma = std();
        for (const auto& s : m_arr) {
            sum += std::pow((s.size() - mu) / sigma, 4);
        }
        return sum / m_size;
    }

    // Jarque-Bera
    double jarqueBera() const {
        double s = skew();
        double k = kurtosis();
        return m_size / 6.0 * (std::pow(s, 2) + (std::pow(k - 3, 2) / 4.0));
    }

    // typeTokenRatio
    double typeTokenRatio() const {
        std::set<std::string> unique{m_arr.begin(), m_arr.end()};
        return static_cast<double>(unique.size()) / m_size;
    }

    // polygrams
    std::map<std::string, int> polygrams(const int& words) const {
        std::map<std::string, int> polygram_count;
        for (size_t i = 0; i <= m_size - words; ++i) {
            std::string word_string = m_arr[i];
            for (int j = 1; j < words; ++j) {
                word_string += " " + m_arr[i + j];
            }
            ++polygram_count[word_string];
        }
        return polygram_count;
    }

    // fashion
    std::string fashion() const {
        std::map<std::string, int> poly = polygrams(1);
        std::string common{};
        int max_value = 0;

        for (const auto& [key, value] : poly) {
            if (value > max_value) {
                max_value = value;
                common = key;
            }
        }

        return common;
    }

    // emotion
    std::map<std::string, int> emotion() const {
        std::map<std::string, int> emotion_map{};

        for (const auto& word : m_arr) {
            for (const auto& pair : emotions) {
                if (word == pair.first) {
                    bool has_key = false;
                    for (auto& map : emotion_map) {
                        if (pair.first == map.first) {
                            ++map.second;
                            has_key = true;
                            break;
                        }
                    }

                    if (!has_key) {
                        emotion_map.insert({pair.second, 1});
                    }
                }
            }
        }

        return emotion_map;
    }

    // reaction
    std::map<std::string, int> reaction() const {
        std::map<std::string, int> reaction_map {
            {"positive", 0},
            {"negative", 0},
            {"neutral", 0}
        };
        std::map<std::string, int> emotion_map = emotion();

        for (const auto& [key, value] : emotion_map) {
            if (std::find(positive_emotion.begin(), positive_emotion.end(), key) != positive_emotion.end()) {
                reaction_map["positive"] += value;
            }

            else if (std::find(negative_emotion.begin(), negative_emotion.end(), key) != negative_emotion.end()) {
                reaction_map["negative"] += value;
            }

            else if (std::find(negative_emotion.begin(), negative_emotion.end(), key) != neutral_emotion.end()) {
                reaction_map["neutral"] += value;
            }
        }

        return reaction_map;
    }
    
    private:

    // members
    std::vector<std::string> m_arr = {};
    double m_size{};
};

#endif