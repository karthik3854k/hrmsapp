<template>
	<div class="flex p-1 bg-[#04161a] rounded-xl border border-[#D4AF37]/40 shadow-inner">
		<button
			v-for="button in buttons"
			:key="button.key ?? button.label ?? button"
			class="py-2.5 px-3 transition-all rounded-lg flex-auto text-xs sm:text-sm text-center font-bold tracking-wide cursor-pointer"
			:class="
				modelValue === (button.key ?? button.label ?? button)
					? 'bg-[#0c3742] text-[#D4AF37] border border-[#D4AF37]/60 shadow-md'
					: 'text-[#E6CA65] hover:text-[#D4AF37] hover:bg-white/[0.05]'
			"
			:style="{
				color: modelValue === (button.key ?? button.label ?? button) ? '#D4AF37' : '#E6CA65'
			}"
			@click="$emit('update:modelValue', button.key ?? button.label ?? button)"
		>
			{{ button.label ?? __(button) }}
		</button>
	</div>
</template>

<script setup>
const props = defineProps({
	buttons: {
		type: Array,
		required: true,
	},
	modelValue: {
		type: String,
	},
})

defineEmits(["update:modelValue"])
</script>
