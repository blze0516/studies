package com.example.backendinterview.lab.day01;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.core.io.ClassPathResource;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public final class Day01DatasetLab {

    private static final String DATASET_PATH = "data/backend_interview_fixed_sample_dataset.json";

    private final JsonNode root;

    public Day01DatasetLab() {
        this.root = loadDataset();
    }

    public String datasetVersion() {
        return root.path("meta").path("dataset_version").asText();
    }

    public int count(String arrayName) {
        JsonNode node = root.path(arrayName);
        if (!node.isArray()) {
            throw new IllegalArgumentException(arrayName + " is not an array field");
        }
        return node.size();
    }

    public String[] productIdsAsArray() {
        JsonNode products = root.path("products");
        String[] ids = new String[products.size()];
        for (int i = 0; i < products.size(); i++) {
            ids[i] = products.get(i).path("product_id").asText();
        }
        return ids;
    }

    public List<String> productIdsAsArrayList() {
        JsonNode products = root.path("products");
        List<String> ids = new ArrayList<>(products.size());
        for (JsonNode product : products) {
            ids.add(product.path("product_id").asText());
        }
        return ids;
    }

    public Optional<ProductView> findProductLinear(String productId) {
        for (JsonNode product : root.path("products")) {
            if (productId.equals(product.path("product_id").asText())) {
                return Optional.of(new ProductView(
                        product.path("product_id").asText(),
                        product.path("name").asText(),
                        product.path("status").asText(),
                        product.path("price").asLong()
                ));
            }
        }
        return Optional.empty();
    }

    private JsonNode loadDataset() {
        ObjectMapper objectMapper = new ObjectMapper();
        ClassPathResource resource = new ClassPathResource(DATASET_PATH);
        try (InputStream inputStream = resource.getInputStream()) {
            return objectMapper.readTree(inputStream);
        } catch (IOException e) {
            throw new IllegalStateException("Failed to load fixed dataset: " + DATASET_PATH, e);
        }
    }

    public record ProductView(String productId, String name, String status, long price) {
    }
}
