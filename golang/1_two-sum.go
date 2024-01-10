// hash 法， 4 ms, 4.02 MB
func twoSum(nums []int, target int) []int {
	temp_map = map[int]int{}
	for index1, value1 := range nums {
		if index2, ok := temp_map[target-value1]; ok {
			return []int{index1, index2}
		}
		temp_map[value1] = index1
	}
	return nil
}